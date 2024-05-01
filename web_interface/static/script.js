const form = document.querySelector('form');


form.addEventListener('submit', function(event) {
    const inputs = document.querySelectorAll('input[type="number"]');
    let hasError = false;

    inputs.forEach(input => {
        if (input.value.trim() === '' || input.value <= 0) {
            input.classList.add('error');
            hasError = true;
        } else {
            input.classList.remove('error');
        }
    });

    if (hasError) {
        event.preventDefault(); 
    }
});
