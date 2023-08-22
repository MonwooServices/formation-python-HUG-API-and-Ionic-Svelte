<script lang="ts">
import { onMount } from 'svelte';
import buddy from '$lib/images/Buddy_Transparent_01.webp';
import { showMenu } from '$lib/services/menu';
import * as allIonicIcons from 'ionicons/icons';
import { goto } from '$app/navigation';
import { menuController, modalController, registerMenu } from 'ionic-svelte';
import { dev } from '$app/environment';
const modules = import.meta.glob('../../**/*.svelte', { as: 'raw' });
let inlineModalOpen = false;
export let side: 'start' | 'end' | undefined = 'start';
$: hideMenu = !$showMenu;

onMount(() => {
		registerMenu('mainmenu');
	});

const closeAndNavigate = async (url: string) => {
		// take the google tag from the main thread
		setTimeout(() => {
			//@ts-ignore
			if (!dev) window.gtag('event', url);
		}, 100);

		console.log('Navigate url', url);

		goto(url);
		menuController.close('mainmenu');
	};
let menuItems: Array<{ url: string; label: string; icon: any }> = Object.keys(modules)
		.filter((key) => key.includes('/routes/') && !key.includes('[tab]'))
		.map((key) =>
			capitalizeFirstLetter(
				key.replace('../../routes/', '').replace('/+page.svelte', '')
			)
		)
		.concat(['buddy'],['debug'],['face'],['history'],['message'],['move'],['test'])
		.sort()

		.map((componentName) => {
			console.log('COMPONENTN', componentName);
			const url =
				componentName !== 'Tabs' ? `${componentName}` : `/`;
			return {
				url,
				label: componentName,
				icon: allIonicIcons['home']
			};
		});

		const icons = Object.keys(allIonicIcons);
	menuItems.map((menuItem) => {
		const iconForMenu = icons[Math.floor(Math.random() * icons.length)];
		// @ts-ignore
		menuItem.icon = allIonicIcons[iconForMenu];
	});
	menuItems = [...menuItems];

		function capitalizeFirstLetter(text: string) {
		return text.charAt(0).toUpperCase() + text.slice(1);
		}
</script>

<ion-menu {side} content-id="main" menu-id="mainmenu" class:menuhide={hideMenu}>
	<ion-modal is-open={inlineModalOpen}>
		<br />

		<ion-content>
			<ion-card>
				<ion-card-header>
					<ion-card-title>Ionic Svelte - Unofficial Ionic integration</ion-card-title>
				</ion-card-header>
				<ion-card-content>
					<p>Ionic-Svelte is work in progress and needs your support.</p>
					<br />
					<p>
						Share how you are using it, what is really working for you and which parts need
						improvement.
					</p>
					<br />
					<p>
						Raise issues on Github - <a
							href="https://github.com/Tommertom/svelte-ionic-app/issues"
							target="_new">https://github.com/Tommertom/svelte-ionic-app/issues</a>
					</p>
					<br />
					<p>
						Join <a
							href="https://discordapp.com/channels/520266681499779082/1049388501629681675"
							target="_new">Ionic-Svelte channel</a> on Ionic's official discord
					</p>
					<br /><br />
					<p>Thanks!!! Tommertom</p>
					<br />
					<img src="/assets/svelte-ionic-logo.png" width="25%" alt="Feedback" />
				</ion-card-content>
			</ion-card>
			<br />
			<ion-button aria-hidden="true"
				expand="block"
				on:keyup={() => {
					inlineModalOpen = false;
				}}
				on:click={() => {
					inlineModalOpen = false;
				}}>
				Close modal
			</ion-button>
			vite v4.
		</ion-content>
	</ion-modal>



	{#if menuItems.length > 0}
		<ion-header>
			<ion-toolbar>
				<ion-title>Menu</ion-title>
				<ion-button aria-hidden="true"
					expand="block"
					on:keyup={() => {
						//@ts-ignore
						window.gtag('event', 'Feedback open');
						inlineModalOpen = true;
					}}
					on:click={() => {
						//@ts-ignore
						window.gtag('event', 'Feedback open');
						inlineModalOpen = true;
					}}
					slot="end">About...</ion-button>
			</ion-toolbar>
		</ion-header>
	<ion-content>
		<ion-list>
			{#each menuItems as menuItem, i}
				<ion-item aria-hidden="true"
					on:keyup={() => {
						closeAndNavigate(menuItem.url);
					}}
					on:click={() => {
						closeAndNavigate(menuItem.url);
					}}>
					<ion-icon icon={menuItem.icon} slot="start" color=black />
					<ion-label>{menuItem.label}</ion-label>
				</ion-item>
				{/each}
				<ion-item />
</ion-list>
</ion-content>
{/if}
</ion-menu>

<style>
	ion-item {
		cursor: pointer;
	}

	.menuhide {
		display: none;
	}
</style>