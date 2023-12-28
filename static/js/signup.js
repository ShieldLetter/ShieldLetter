(() => {
  function checkInputs() {
    var nameValue = document.getElementById('floatingName').value;
    var idValue = document.getElementById('floatingId').value;
    var passwordValue = document.getElementById('floatingPassword').value;
    var submitButton = document.querySelector('.btn-primary');

    submitButton.disabled = nameValue === '' || idValue === '' || passwordValue === '';
  }

  document.getElementById('floatingName').addEventListener('input', checkInputs);
  document.getElementById('floatingId').addEventListener('input', checkInputs);
  document.getElementById('floatingPassword').addEventListener('input', checkInputs);
})();
