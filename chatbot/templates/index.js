// Show the loading spinner
function showSpinner() {
    const spinner = document.createElement('div');
    spinner.classList.add('spinner-border', 'text-primary', 'mx-auto');
    spinner.setAttribute('role', 'status');
    document.querySelector('#chatbot-response').appendChild(spinner);
}

// Hide the loading spinner
function hideSpinner() {
    const spinner = document.querySelector('.spinner-border');
    spinner.parentNode.removeChild(spinner);
}
