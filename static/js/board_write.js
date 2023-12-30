(() => {
    // form 유효성 검사
    function validateForm() {
        var title = document.getElementById('title').value.trim(); // title에서 공백 제거
        var content = document.getElementById('content').value.trim(); // content에서 공백 제거
        var fileInput = document.getElementById('file');
        var filePath = fileInput.value;
        var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i; // 허용되는 파일 확장자 정의
        var submitButton = document.getElementById('submit');
        // 제목이나 내용이 없거나 허용되지 않는 파일 확장자인 경우
        if (!title || !content || !allowedExtensions.exec(filePath)) {
            submitButton.disabled = true; // 전송 버튼 비활성화
            return false;
        } else {
            submitButton.disabled = false; // 전송 버튼 활성화
            return true;
        }
    }
    // title, content, file 부분에 입력이나 변경 발생할 때마다 유효성 검사 실행
    document.getElementById('title').addEventListener('input', validateForm);
    document.getElementById('content').addEventListener('input', validateForm);
    document.getElementById('file').addEventListener('change', validateForm);
})();
