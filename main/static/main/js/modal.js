$('.modal-overlay, .modal').hide()

login_form = $('#login.modal')
signup_form = $('#signup.modal')

$('.modal-overlay, .modal-close').click(function(){
    $('.modal, .modal-overlay').hide()
})

$('.navigator__login').click(function(){
    $('#login.modal , .modal-overlay').show()
})

$('#login.modal #change').click(function(){
    login_form.hide()
    $('#signup.modal, .modal-overlay').show()
})