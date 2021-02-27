let myId;

async function requestHistorySince(index) {
	while (true) {
		try {
			var resp = await fetch(`/api/history?since=${index}`);
			var data = await resp.json();
			return data
		} catch { }
	}
}

async function requestOptions() {
	while (true) {
		try {
			var resp = await fetch("/api/options");
			var data = await resp.json();
			const index = data.round;
			const options = data.options;
			
			return [index, options];
		} catch { }
	}
}

async function castVote(optionIndex,round) {
	while (true) {
		try {
			return await fetch(`/api/vote?id=${myId}&opt=${optionIndex}&round=${round}`,{"method":"POST"});
		} catch { }
	}
}
