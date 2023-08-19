<svelte:head>
<title>Ionic Companion - Message</title>
<meta name="Message" content="Send message" />
</svelte:head>

<script lang="ts">
import { loadingController } from 'ionic-svelte';
import { toastController } from 'ionic-svelte';
let text:any="testnok";

const showToast = async (color:any,message:any) => {
	const toast = await toastController.create({
		color: color,
		duration: 4000,
		message: message
		});
	toast.present();
	};

	const showLoading = async () => {
		const options = {
		message: 'Loading......',
		duration: 30000
		};
		const loading = await loadingController.create(options);
		loading.present();
		setTimeout(() => {
			loading.dismiss();
			}, 2500);	
		};
		
async function submit(text:any) {
		showLoading();
		console.log(text.text.value)
		const queryString = window.location.search;
		const urlParams = new URLSearchParams(queryString);
		const backendIp = urlParams.get("backendIp") || "192.168.1.100";
		const backendPort = urlParams.get("backendPort") || "8000";

		await fetch(`http://${backendIp}:${backendPort}/api/buddy/send-msg`, {
        method: "POST",
        body: JSON.stringify({
            msg: text.text.value
        }),
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
      }).then(
        async resp => {
          const dataResp = await resp.json(); // this returns a promise
		  return resp;
        }).then(repos => {
			setTimeout(() => {
				showToast("success","Succès de l'envoi");
			}, 2200);
          console.log(repos)
        }).catch(ex => {
			showToast("danger","Echec de l'envoi");
          console.error(ex);
        })
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

	<ion-item>
		<ion-input clear-input bind:this={text} label="Entrer votre message !" label-placement="floating" name="Message" />
	</ion-item>
		</ion-card>

	<div class="ion-padding">
		<ion-button role="presentation" on:click={ () => (submit({text})) } expand="block" type="submit" class="ion-no-margin"> Envoyer </ion-button>
	</div>

	</ion-content>
  
	


	