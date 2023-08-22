<svelte:head>
	<title>Ionic Companion - Presentation</title>
	<meta name="Buddy" content="Robot tools" />
</svelte:head>
	
<script lang="ts">
	import littlestar_love from '$lib/images/faces/18_littlestar_love.gif'
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
		<ion-img src={littlestar_love} alt="littlestar_love"></ion-img>
	</ion-item>
	</ion-card>
</ion-content>