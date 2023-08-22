<svelte:head>
	<title>Ionic Companion - Debug</title>
	<meta name="Debug Mode" content="Check configuration" />
</svelte:head>

<script lang="ts">
	import { alertController } from 'ionic-svelte';

	async function showAlert(options:any) {
		const alert = await alertController.create(options);
		alert.present();
	};

	function showSimpleAlert() {
		const options = {
			header: 'Test',
			subHeader: '',
			message: 'Commande lancée.',
			buttons: ['OK']
		};
		return showAlert(options);
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
			<ion-title>Debug</ion-title>
	 </ion-toolbar>
	 </ion-header>
	<ion-card>
		<ion-card-header>
		<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
		<!--<ion-card-title>DEBUG MODE</ion-card-title>-->
	</ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>

	<ion-item>
		<ion-label>Test 1</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>

	<ion-item>
		<ion-label>Test 2</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 3</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 4</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 5</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 6</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 7</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 8</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	<ion-item>
		<ion-label>Test 9</ion-label>
		<ion-button role="presentation" fill="outline" on:click={showSimpleAlert}> View </ion-button>
	</ion-item>
	</ion-card>

</ion-content>
  