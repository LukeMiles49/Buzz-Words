const storyElement = document.getElementById('story');
const optionsElement = document.getElementById('options');

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function app() {
	const story = [];
	
	while (true) {
		// Load new paragraphs
		let newParagraphs = await requestHistorySince(story.length);
		while (newParagraphs.length == 0) {
			await sleep(1000);
			newParagraphs = await requestHistorySince(story.length);
		}
		
		// Render new paragraphs
		for (const paragraph of newParagraphs) {
			const element = document.createElement('p');
			element.innerText = paragraph;
			story.push(paragraph);
			storyElement.appendChild(element);
		}
		
		// Clear previous options
		optionsElement.innerHTML = '';
		
		const currentRound = story.length;
		
		// Load new options
		const [roundID, options] = await requestOptions();
		
		if (roundID === currentRound) {
			// Render options
			const optionElements = [];
			for (const optionIndex in options) {
				const element = document.createElement('p');
				element.innerText = options[optionIndex];
				element.onclick = () => {
					castVote(optionIndex, currentRound);
					for (const opt of optionElements) {
						opt.classList.remove('enabled');
					}
				};
				element.classList.add('enabled');
				optionElements.push(element);
				optionsElement.appendChild(element);
			}
		}
	}
}

app();
