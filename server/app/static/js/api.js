let myId;

async function requestHistorySince(index) {
	var resp = await fetch("/api/history?since");
	var data = await resp.json();
	return data
}

async function requestOptions() {
	var resp = await fetch("/api/options");
	var data = await resp.json();
	const index = data.round;
	const options = data.options;
	
	return [index, options];
}

async function castVote(optionIndex,round) {
	// TODO
	return (await fetch(`/api/vote?id=${myId}&opt=${optionIndex}&round=${round}`,{"method":"POST"}));
}
