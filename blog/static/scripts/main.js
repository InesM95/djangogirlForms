function editPost(id) {
    if (id) {
        $.ajax({
            url: `edit/`, // the endpoint
            type: "GET", // http method
            // handle a successful response
            success: function (response) {
                $('#formContent').html(response.form);
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
}


function deletePost(id) {
    var serializedData = $('#formModal').serializeArray();
    $.ajax({
        url: `post/${id}/delete/`, // the endpoint
        type: "POST", // http method
        data: serializedData, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $(`#deletePostModal${id}`).modal('hide');
            $(`#post${id}`).remove();
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

$(document).ready(function () {
    $("#editPostBtnSave").click(function () {
        console.log($("form").serializeArray());
        dataForm =$("form").serializeArray()
        $.ajax({
            url: `edit/`, // the endpoint
            type: "POST", // http method
            data: dataForm,
            // handle a successful response
            success: function (response) {
                if (!(response['success'])) {
                    $("form").replaceWith(response['form_html']);
                } else {
                $("#editPostModal").modal('hide');
                $("#titleInput").text(dataForm[1]['value'])
                $("#textInput").text(dataForm[2]['value'])
                }
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
});
