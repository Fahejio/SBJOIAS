// const getElement = (...queries) => document.querySelector(...queries);

// const button = getElement('.open-modal-button');
// const container = getElement('.modal_pai');
// const modal = getElement('.modal_filho');
// const activeModalClass = 'modal-show';

// const OpenModal = () => container.classList.add(activeModalClass);
// const closeModal = () => {};

// button.addEventListener('click', OpenModal)
const getElement = (...queries) => document.querySelector(...queries);

const button = getElement('.open-modal-button');
const container = getElement('.modal-container');
const modal = getElement('.modal');

const activeModalClass = 'modal-show';

const openModal = () => container.classList.add(activeModalClass);
const closeModal = () => container.classList.remove(activeModalClass);

button.addEventListener('click', openModal);
container.addEventListener('click', (event) => {
	if (modal.contains(event.target)) return;
	
	closeModal();
});
