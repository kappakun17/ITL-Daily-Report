var elm_pass = $('#password');
var elm_confirm = $('#confirm-password');
/*
* �m�F�p�X���[�h�̃L�[�{�[�h�iKeyUp�j�C�x���g���X�i�[
*/
elm_confirm.on('keyup', function () {
    // �܂��p�X���[�h�i�m�F�j����͂��Ă��Ȃ�
    if (elm_confirm.val() === "") {
        elm_confirm.removeClass("is-valid");
        elm_confirm.removeClass("is-invalid");
        return;
    }
    // �擪����ꕶ�������o���ă`�F�b�N���Ō�܂œ��B���Ă��Ȃ��Ƃ��u��薳���v�Ɣ��f
    var array_pass_chars = elm_pass.val().split("");
    var array_confirm_chars = elm_confirm.val().split("");
    $.each(array_confirm_chars, function (index, char) {
        if (array_pass_chars[index] === char) {
            // �擪����ꕶ������v���Ă���ꍇ�ɂ͒��r�ł������\�����Ȃ�
            elm_confirm.removeClass("is-valid");
            elm_confirm.removeClass("is-invalid");
        }
        else {
            // �ꕶ���ł��قȂ�ꍇ��Invalid
            elm_confirm.removeClass("is-valid");
            elm_confirm.addClass("is-invalid");
            return false;
        }
    });
    // ���S��v������Valid
    if (elm_pass.val() === elm_confirm.val()) {
        elm_confirm.addClass("is-valid");
    }
});
/*
* �m�F�p�X���[�h���͂̃t�H�[�J�X���������Ƃ��iBlur�j�̃C�x���g���X�i�[
*/
elm_confirm.on('blur', function () {
    // �p�X���[�h���͗��̗�������̂Ƃ��̓o���f�[�V�����\��������
    if (elm_pass.val() === "" && elm_confirm.val() === "") {
        elm_pass.removeClass('is-valid');
        elm_pass.removeClass('is-invalid');
        elm_confirm.removeClass('is-valid');
        elm_confirm.removeClass('is-invalid');
        return;
    }
    // ���S��v������Valid
    if (elm_pass.val() === elm_confirm.val()) {
        elm_confirm.removeClass('is-invalid');
        elm_confirm.addClass("is-valid");
    }
    else {
        // ��v���Ȃ�������Invalid
        elm_confirm.removeClass('is-valid');
        elm_confirm.addClass("is-invalid");
    }
});
/*
* �p�X���[�h���͂̃t�H�[�J�X���������Ƃ��iBlur�j�̃C�x���g���X�i�[
* ���͂��ꂽ�p�X���[�h���K�؂Ȃ��̂��`�F�b�N����
*/
elm_pass.on('blur', function () {
    // �p�X���[�h���͗��̗�������̂Ƃ��̓o���f�[�V�����\��������
    if (elm_pass.val() === "" && elm_confirm.val() === "") {
        elm_pass.removeClass('is-valid');
        elm_pass.removeClass('is-invalid');
        elm_confirm.removeClass('is-valid');
        elm_confirm.removeClass('is-invalid');
        return;
    }
    var str = elm_pass.val();
    // ���p�p���������ꂼ��1��ވȏ�܂�8�����ȏ�̕�����ƃ}�b�`���邩
    var result = str.match(/^(?=.*?[a-zA-Z])(?=.*?\d)[a-zA-Z\d]{8,}/);
    if (result) {
        // O.K.�iValid�j
        elm_pass.removeClass('is-invalid');
        elm_pass.addClass('is-valid');
    }
    else {
        // ���͂��ꂽ�p�X���[�h����v���܂���B�iInvalid�j
        elm_pass.removeClass('is-valid');
        elm_pass.addClass('is-invalid');
    }
});

var elm_email = $('#email')
var elm_confirm_email = $('#confirm-email');
/*
* �m�Femail��keyup 
*/
elm_confirm_email.on('keyup', function () {
    // �܂����[���A�h���X�i�m�F�j����͂��Ă��Ȃ�
    if (elm_confirm_email.val() === "") {
        elm_confirm_email.removeClass("is-valid");
        elm_confirm_email.removeClass("is-invalid");
        return;
    }
    // �擪����ꕶ�������o���ă`�F�b�N���Ō�܂œ��B���Ă��Ȃ��Ƃ��u��薳���v�Ɣ��f
    var array_email_chars = elm_email.val().split("");
    var array_confirm_email_chars = elm_confirm_email.val().split("");
    $.each(array_confirm_email_chars, function (index, char) {
        if (array_email_chars[index] === char) {
            // �擪����ꕶ������v���Ă���ꍇ�ɂ͒��r�ł������\�����Ȃ�
            elm_confirm_email.removeClass("is-valid");
            elm_confirm_email.removeClass("is-invalid");
        }
        else {
            // �ꕶ���ł��قȂ�ꍇ��Invalid
            elm_confirm_email.removeClass("is-valid");
            elm_confirm_email.addClass("is-invalid");
            return false;
        }
    });
    // ���S��v������Valid
    if (elm_email.val() === elm_confirm_email.val()) {
        elm_confirm_email.addClass("is-valid");
    }
});
/*
* �m�F���[���A�h���X���͂̃t�H�[�J�X���������Ƃ��iBlur�j�̃C�x���g���X�i�[
*/
elm_confirm_email.on('blur', function () {
    // ���[���A�h���X���͗��̗�������̂Ƃ��̓o���f�[�V�����\��������
    if (elm_email.val() === "" && elm_confirm_email.val() === "") {
        elm_email.removeClass('is-valid');
        elm_email.removeClass('is-invalid');
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.removeClass('is-invalid');
        return;
    }
    // ���S��v������Valid
    if (elm_email.val() === elm_confirm_email.val()) {
        elm_confirm_email.removeClass('is-invalid');
        elm_confirm_email.addClass("is-valid");
    }
    else {
        // ��v���Ȃ�������Invalid
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.addClass("is-invalid");
    }
});
/*
* email���͂̃t�H�[�J�X���������Ƃ��iBlur�j�̃C�x���g���X�i�[
* ���͂��ꂽ���[���A�h���X���K�؂Ȃ��̂��`�F�b�N����
*/
elm_email.on('blur', function () {
    // email���͗��̗�������̂Ƃ��̓o���f�[�V�����\��������
    if (elm_email.val() === "" && elm_confirm_email.val() === "") {
        elm_email.removeClass('is-valid');
        elm_email.removeClass('is-invalid');
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.removeClass('is-invalid');
        return;
    }
    var str = elm_email.val();
    // ���p�p���������ꂼ��1��ވȏ�܂�8�����ȏ�̕�����ƃ}�b�`���邩
    //���K�\���́AMicrosoft�Ј�����ɐݒ肵�Ă���B�X�^�b�t�T�C���A�b�v�͕ς���K�v
    var result = str.match(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}microsoft.com$/);
    if (result) {
        // O.K.�iValid�j
        elm_email.removeClass('is-invalid');
        elm_email.addClass('is-valid');
    }
    else {
        // ���͂��ꂽ�A�h���X����v���܂���B�iInvalid�j
        elm_email.removeClass('is-valid');
        elm_email.addClass('is-invalid');
    }
});