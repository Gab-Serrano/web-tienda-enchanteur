const updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    const productId = this.dataset.product;
    const action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);

    console.log("USER:", user);
    if (user === "AnonymousUser") {
      console.log("Not logged in");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data...");

  const url = "/update_item/";
  var responseClone;
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      console.log("response:", response); // Add this line to check the response
      responseClone = response.clone();
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload()},function (rejectionReason) { // 3
        console.log('Error parsing JSON from response:', rejectionReason, responseClone); // 4
        responseClone.text() // 5
        .then(function (bodyText) {
            console.log('Received the following instead of valid JSON:', bodyText); // 6
        });
    });
}

