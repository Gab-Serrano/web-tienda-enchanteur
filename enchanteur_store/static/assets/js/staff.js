/* function validateForm() {
    var name = document.getElementById('id_name').value;
    var description = document.getElementById('id_description').value;

    if (description.length > 200) {
        document.getElementById('description-error').textContent = 'La descripción no puede tener más de 200 caracteres.';
        return false;
    }
    return true;
} */

(() => {
    console.log('staff.js loaded');
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
        console.log(form.classList);
      }, false)
    })
  })()