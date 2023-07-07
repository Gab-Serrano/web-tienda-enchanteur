(() => {
    console.log('checkout.js loaded');
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    console.log(forms);
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        event.preventDefault()
        if (!form.checkValidity()) {
          event.stopPropagation()
        }
        else {
            document.getElementById('form-button').classList.add("hidden");
            document.getElementById('payment-info').classList.remove("hidden");
        }
  
        form.classList.add('was-validated')
        console.log(form.classList);
      }, false)
    })
  })()

if (user != 'AnonymousUser') {
    document.getElementById('user-info').innerHTML = ''
}

/* var form = document.getElementById('form')
form.addEventListener('submit', function (e) {
    e.preventDefault()
    document.getElementById('form-button').classList.add("hidden");
    document.getElementById('payment-info').classList.remove("hidden");
}) */

document.getElementById('make-payment').addEventListener('click', function (e) {
    submitFormData()
})

function submitFormData() {
    console.log('Payment button clicked')

    var userFormData = {
        'name': null,
        'email': null,
        'total': total,
    }

    var shippingInfo = {
        'address': null,
        'city': null,
        'state': null,
        'country': null,
        'zipcode': null,
    }

    shippingInfo.address = form.address.value
    shippingInfo.city = form.city.value
    shippingInfo.state = form.state.value
    shippingInfo.country = form.country.value
    shippingInfo.zipcode = form.zipcode.value

    if (user == 'AnonymousUser') {
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }
    console.log('Shipping Info:', shippingInfo)
    console.log('User Info:', userFormData)

    var url = "/process_order/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'form': userFormData, 'shipping': shippingInfo}),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data)
        cart = {}
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        window.location.href = '/store/'
    })
}