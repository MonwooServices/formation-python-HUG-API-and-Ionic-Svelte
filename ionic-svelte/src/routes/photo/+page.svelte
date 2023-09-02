<svelte:head>
<title>Ionic Companion - Message</title>
<meta name="Message" content="Send message" />
</svelte:head>

<script lang="ts">
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
	import { image } from 'ionicons/icons';

async function takePhoto() {
  const image = await Camera.getPhoto({
    quality: 90,
    allowEditing: false,
    resultType: CameraResultType.Uri, // Définissez le type de résultat sur Uri
    source: CameraSource.Camera,
  });

  // Faites quelque chose avec l'image capturée :
  const imageUrl = image.webPath;

  
  if (imageUrl) {
	console.log('Image URL:', imageUrl);
    // Traitez l'URL de l'image ici
  }
}
</script>

	<ion-content fullscreen class="ion-padding">
		<ion-header translucent={true}>
		  <ion-toolbar>
			<ion-buttons slot="start">
			  <ion-menu-button />
			</ion-buttons>
			<ion-buttons slot="end">
			</ion-buttons>
				<ion-title>Message</ion-title>
		 </ion-toolbar>
     	</ion-header>
		<ion-card>
		  <ion-card-header>
			<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
			<!--<ion-card-title>MESSAGE</ion-card-title>-->
		  </ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>
		</ion-card>

	<div class="ion-padding">
		<ion-button role="presentation" on:click={ () => (takePhoto()) } expand="block" type="submit" class="ion-no-margin"> Envoyer </ion-button>
	</div>
	<ion-img src={image} alt="buddy faces"></ion-img>
	</ion-content>