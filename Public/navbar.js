// toggling dropdown
const profile = document.querySelector('.profileContainer');
const dropdown = document.querySelector('.dropdownContainer');

profile.addEventListener('click', () => {
    dropdown.classList.toggle('active');
});
