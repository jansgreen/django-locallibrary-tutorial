

// A reference to Stripe.js initialized with your real test publishable API key.
var PublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_stripe_client_secret').text().slice(1, -1);
var intent = $('#id_intent').text().slice(1, -1)
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
/* form submit*/

var form = document.querySelector("payment-form");

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $('#button-submit').attr('disabled', true);
  stripe.confirmCardPayment(intent, {
      payment_method: {
        card: card,
      },
    }).then(function (result) {
      if (result.error) {
        var errorDiv = document.getElementById('card-error');
        var html = `<span class ="icon" role="alert"> <i class="fa fa-times"></i></span> <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({ disabled: true });
        $("#submit-button").attr("disabled", true);
      } else {
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
          // Complete payment when the submit button is clicked

        }
      }
    });
});
