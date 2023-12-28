(() => {
    function checkInputs() {
      var idValue = document.getElementById('floatingId').value;
      var passwordValue = document.getElementById('floatingPassword').value;
      var submitButton = document.getElementById('loginBtn');
  
      submitButton.disabled = idValue === '' || passwordValue === '';
    }

    document.getElementById('floatingId').addEventListener('input', checkInputs);
    document.getElementById('floatingPassword').addEventListener('input', checkInputs);
  
})();
  