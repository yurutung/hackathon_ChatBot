//取得當前時間
function get_current_time() {
    today = new Date()
    date_time = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate() + ' '+ today.getHours() + ":" + today.getMinutes()
    return date_time
}

// 將訊息視窗的scrollbar保持在置底
function message_bottom() {
    msg_block = document.getElementById('message_block')
    msg_block.scrollTop = msg_block.scrollHeight
}

//顯示chatbot輸出的文字
function show_chatbot_msg(msg) {
    $('#message_block').append(
        '<div class="d-flex justify-content-start mb-4">' +
            '<div class="msg_cotainer" >' + msg + '<span class="msg_time">' + get_current_time() + '</span>' + '</div>' +
        '</div>')
    message_bottom()
}

//顯示使用者輸入的文字
function show_user_msg(msg) {
    $('#message_block').append(
        '<div class="d-flex justify-content-end mb-4">' +
            '<div class="msg_cotainer_send">' + msg + '<span class="msg_time_send">' + get_current_time() + '</span>' + '</div>' +
        '</div>')
    message_bottom()
}

// 將過去的options disabled
function option_disabled() {
    $(".option").find("button").attr('disabled', 'disabled')
    $(".option").find("button").removeAttr('id')
}

//顯示Chatbot功能選項
function chat_bot_options() {
    try{
        option_disabled()
    }
    finally{
        $('#message_block').append(
            '<div class="d-flex justify-content-start mb-4 option">' +
                '<div class="btn-group-vertical btn-group">' +
                    '<button type="button" class="btn btn-link" id = "option1" value="say_hi">say_hi</button>' +
                    '<button type="button" class="btn btn-link" id = "option2" value="get_google">google</button>' +
                    '<span class="msg_time">' + get_current_time() + '</span>' +
                '</div>' +
            '</div>')
    }
    message_bottom()
}
