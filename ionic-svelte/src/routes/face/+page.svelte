<svelte:head>
	<title>Ionic Companion - Presentation</title>
	<meta name="Buddy" content="Robot tools" />
</svelte:head>
	
<script lang="ts">
	import './styles.css';
	import buddy_static from '$lib/images/faces/47_static.gif'
	import buddy_sad from '$lib/images/faces/48_sad.gif'
	import buddy_scared from '$lib/images/faces/49_scared.gif'
	import buddy_sick from '$lib/images/faces/50_sick.gif'
	import littlestar_love from '$lib/images/faces/18_littlestar_love.gif'
	let face =buddy_static;

	function changeFace(next_face:any) {
		face=next_face
		console.log(face)
		return face;
	};
</script> 

<ion-content fullscreen class="ion-padding">
	<ion-header translucent={true}>
	  <ion-toolbar>
		<ion-buttons slot="start">
		  <ion-menu-button />
		</ion-buttons>
		<ion-buttons slot="end">
		</ion-buttons>
			<ion-title>Buddy Faces</ion-title>
	  </ion-toolbar>
	</ion-header>
	<ion-card>
		<ion-card-header>
		<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
		<!--<ion-card-title>HISTORY</ion-card-title>-->
		</ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>
	<ion-item>
	  <ion-img src={face} alt="buddy faces"></ion-img>
	</ion-item>
	<ion-list>
	  <ion-item>
		<ion-button role="presentation" fill="clear" on:click={ () => (changeFace(buddy_static))}>
		  <ion-thumbnail slot="start">
			<ion-img src={buddy_static}></ion-img>
		  </ion-thumbnail>
		  <ion-label>buddy_static</ion-label>
		</ion-button>
	  </ion-item>
	  <ion-item>
		<ion-button role="presentation" fill="clear" on:click={ () => (changeFace(buddy_sad))}>
		  <ion-thumbnail slot="start">
			<ion-img src={buddy_sad}></ion-img>
		  </ion-thumbnail>
		  <ion-label>buddy_sad</ion-label>
		</ion-button>
	  </ion-item>
	  <ion-item>
		<ion-button role="presentation" fill="clear" on:click={ () => (changeFace(buddy_scared)) }>
		  <ion-thumbnail slot="start">
			<ion-img src={buddy_scared}></ion-img>
		  </ion-thumbnail>
		  <ion-label>buddy_scared</ion-label>
		</ion-button>
	  </ion-item>
	  <ion-item>
		<ion-button role="presentation" fill="clear" on:click={ () => (changeFace(buddy_sick))}>
		  <ion-thumbnail slot="start">
			<ion-img src={buddy_sick}></ion-img>
		  </ion-thumbnail>
		  <ion-label>buddy_sick</ion-label>
		</ion-button>
	  </ion-item>
	  <ion-item>
		<ion-button role="presentation" fill="clear" on:click={ () => (changeFace(littlestar_love))}>
		  <ion-thumbnail slot="start">
			<ion-img src={littlestar_love}></ion-img>
		  </ion-thumbnail>
		  <ion-label >littlestar_love</ion-label>
		</ion-button>
	  </ion-item>
	</ion-list>
	</ion-card>
</ion-content>
