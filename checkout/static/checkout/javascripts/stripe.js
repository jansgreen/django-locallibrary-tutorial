// A reference to Stripe.js initialized with your real test publishable API key.
var PublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_stripe_client_secret').text().slice(1, -1);
var stripe = Stripe(PublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: "#3a7ba0",
    fontFamily: "Arial, sans-serif",
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {},
  },
  invalid: {
    fontFamily: "Arial, sans-serif",
    color: "#fa755a",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-error");
  if (event.error) {
    var html = `<span class ="icon" role="alert"> <i class="fa fa-times"></i></span> <span>${event.error.message}</span>`;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});
/* form suminit*/

var form = document.getElementById("payment-form");
console.log(form + " Entrando a profudidades");

form.addEventListener('submit', function(event) {
  console.log( "profundidad 2");
  event.preventDefault();
  card.update({ disabled: true });
  $('submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
      },
    }).then(function (result) {
      console.log("profundidad 4");
      if (result.error) {
        var errorDiv = document.getElementById('card-error');
        var html = `<span class ="icon" role="alert"> <i class="fa fa-times"></i></span> <span>${event.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({ disabled: true });
        $("#submit-button").attr("disabled", true);
      } else {
        if (result.paymentInttent.status === "succeeded") {
          form.submit();
          console.log("sended");
          // Complete payment when the submit button is clicked

          payWithCard(stripe, card, data.clientSecret);
        }
      }
    });
});
