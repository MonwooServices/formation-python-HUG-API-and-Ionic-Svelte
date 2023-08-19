<script lang="ts">
	import Keypad from './Keypad.svelte';

	let pin:any;
	$: view = pin
		? pin.replace(/\d(?!$)/g, '•')
		: 'enter your pin';

	function handleSubmit() {
		alert(`submitted ${pin}`);
	}
</script>

<h1 style="opacity: {pin ? 1 : 0.4}">
	{view}
</h1>

<Keypad
	bind:value={pin}
	on:submit={handleSubmit}
/>
