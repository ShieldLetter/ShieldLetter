(() => {
    function validateForm() {
        var title = document.getElementById('title').value.trim();
        var content = document.getElementById('content').value.trim();
        var fileInput = document.getElementById('file');
        var filePath = fileInput.value;
        var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
        var submitButton = document.getElementById('submit');

        var existingFile = '{{ board.file.name|basename }}';
        var existingFileExtension = existingFile.split('.').pop();

        if (!title || !content || (!allowedExtensions.exec(filePath) && !allowedExtensions.exec(existingFileExtension))) {
            submitButton.disabled = true;
            return false;
        } else {
            submitButton.disabled = false;
            return true;
        }
    }

    document.getElementById('title').addEventListener('input', validateForm);
    document.getElementById('content').addEventListener('input', validateForm);
    document.getElementById('file').addEventListener('change', validateForm);
})();
