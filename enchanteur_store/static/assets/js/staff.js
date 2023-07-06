function validateForm() {
    var description = document.getElementById('id_description').value;
    if (description.length > 200) {
        document.getElementById('description-error').textContent = 'La descripción no puede tener más de 200 caracteres.';
        return false;
    }
    return true;
}

function showMessage(message, isSuccess) {
    const messageContainer = document.getElementById('message-container');
    messageContainer.innerHTML = message;
    messageContainer.className = isSuccess ? 'success' : 'error';
    messageContainer.style.display = 'block';
    setTimeout(function () {
        messageContainer.style.display = 'none';
    }, 3000); // 3 segundos (ajusta este valor según tus preferencias)
}