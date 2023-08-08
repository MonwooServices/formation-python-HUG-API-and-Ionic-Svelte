<script lang="ts">

	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
    import { onMount } from 'svelte';
	let message:any;
	let inputText:HTMLInputElement;
	//onMount(() => {
		//const queryString = window.location.search;
		//const urlParams = new URLSearchParams(queryString);
		//const backendIp = urlParams.get("backendIp") || "86.193.154.93";
		//const backendPort = urlParams.get("backendPort") || "8000";
	//})
	async function change(message:any) {
		const queryString = window.location.search;
		const urlParams = new URLSearchParams(queryString);
		const backendIp = urlParams.get("backendIp") || "86.193.154.93";
		const backendPort = urlParams.get("backendPort") || "8000";

		await fetch(`http://${backendIp}:${backendPort}/api/buddy/send-msg`, {
        method: "POST",
        body: JSON.stringify({
            msg: message
        }),
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
      }).then(
        async resp => {
          const dataResp = await resp.json(); // this returns a promise
          // TODO
          return resp;
        }).then(repos => {
          console.log(repos)
        }).catch(ex => {
          console.error(ex);
        })
	
		await fetch(`http://${backendIp}:${backendPort}/api/buddy/read-msgs`).then(
        async resp => {
          const dataResp = await resp.json(); // this returns a promise
          const messageList = dataResp.buddy_messages
		  const lastMessage = messageList[messageList.length-1]
          if (message == lastMessage) {
            console.log(message);}
          return resp;
        }).then(repos => {
          console.log(repos)
        }).catch(ex => {
          console.error(ex);
        })

	}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		to<br />buddy application
	</h1>
	<h1>
		<input type="text" bind:this={inputText}>
	</h1>
	<div class="testButton">
		<button on:click={ () => (change(message = inputText.value)) }>
			Cliquez-moi
		  </button>
	<div/>
	<p>
		Envoi du message "{message}" !!!
	</p>
	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2>

	<Counter />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
