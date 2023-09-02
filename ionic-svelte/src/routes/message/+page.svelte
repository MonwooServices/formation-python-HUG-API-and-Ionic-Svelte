<svelte:head>
<title>Ionic Companion - Message</title>
<meta name="Message" content="Send message" />
</svelte:head>

<script lang="ts">
import { loadingController } from 'ionic-svelte';
import { toastController } from 'ionic-svelte';
let ionInput:any="";
let textValue="";

async function showToast(color:any,message:any) {
	const toast = await toastController.create({
		color: color,
		duration: 4000,
		message: message
		});
	toast.present();
	ionInput.value = '';
	};

	async function showLoading() {
		const options = {
		message: 'Loading......',
		duration: 3000
		};
		const loading = await loadingController.create(options);
		loading.present();
		setTimeout(() => {
			loading.dismiss();
			}, 2500);
		};
		
async function submit(ionInput:any) {
		showLoading();
		const queryString = window.location.search;
		const urlParams = new URLSearchParams(queryString);
		const backendIp = urlParams.get("backendIp") || "192.168.1.100";
		const backendPort = urlParams.get("backendPort") || "8000";

		await fetch(`http://${backendIp}:${backendPort}/api/buddy/send-msg`, {
        method: "POST",
        body: JSON.stringify({
            msg: ionInput.value
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
		<ion-input on:input={() => {
			textValue=ionInput.value;
		
		}} bind:this={ionInput} label="Entrer votre message !" label-placement="floating" name="Message" />
	</ion-item>
		</ion-card>

	<ion-item>
		<ion-button disabled={!textValue.length} id="but" role="presentation" on:click={ () => (submit(ionInput)) }> Envoyer </ion-button>
	</ion-item>

	</ion-content>