// script.js (JavaScript)
$(document).ready(function() {
    $('#generate-button').click(function() {
        $.ajax({
            url: '/generate_code',
            success: function(data) {
                $('#code-span').text(data.code);
            }
        });
    });
});
