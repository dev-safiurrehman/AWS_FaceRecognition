// $(document).ready(function() {
//     $('#upload-form').on('submit', function(event) {
//         event.preventDefault();
//         var form_data = new FormData($('#upload-form')[0]);
//         $.ajax({
//             type: 'POST',
//             url: '/upload',
//             data: form_data,
//             contentType: false,
//             cache: false,
//             processData: false,
//             success: function(data) {
//                 $('#message').html('<p>' + data.message + '</p>');
//                 loadAttendanceRecords();
//             },
//         });
//     });
// });

// function loadAttendanceRecords() {
//     $.ajax({
//         type: 'GET',
//         url: '/attendance',
//         success: function(data) {
//             var records_html = '<ul>';
//             for (var i = 0; i < data.length; i++) {
//                 records_html += '<li>Student: ' + data[i].student_id + ', Date: ' + data[i].date + '</li>';
//             }
//             records_html += '</ul>';
//             $('#attendance-records').html(records_html);
//         },
//     });
// }

// $(document).ready(function() {
//     loadAttendanceRecords();
// });

$(document).ready(function() {
    $('#upload-form').on('submit', function(event) {
        event.preventDefault();
        var form_data = new FormData($('#upload-form')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                alert(data.message);  // Display the message in an alert box
                loadAttendanceRecords();
            },
        });
    });
});

function loadAttendanceRecords() {
    $.ajax({
        type: 'GET',
        url: '/attendance',
        success: function(data) {
            var records_html = '<ul>';
            for (var i = 0; i < data.length; i++) {
                records_html += '<li>Student: ' + data[i].student_id + ' is Present ' +', Date: ' + data[i].date + '</li>';
            }
            records_html += '</ul>';
            $('#attendance-records').html(records_html);
        },
    });
}

$(document).ready(function() {
    loadAttendanceRecords();
});
