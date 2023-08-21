<svelte:head>
<title>Ionic Companion - Debug</title>
<meta name="Horn" content="Play mp3" />
</svelte:head>

<script lang="ts">
	import { IonPage } from 'ionic-svelte';
	import BigRedButton from './BigRedButton.svelte';
	import horn from './horn.mp3';

	const audio = new Audio();
	audio.src = horn;

	function handleClick() {
		audio.play();
	}
</script>

<IonPage>
	<ion-header translucent={true}>
		<ion-toolbar>
			<!--<ion-title>Debug</ion-title>-->
		</ion-toolbar> 
	</ion-header>
	<center><BigRedButton on:click={handleClick()}  /></center>
</IonPage>
