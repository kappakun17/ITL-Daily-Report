var elm_pass = $('#password');
var elm_confirm = $('#confirm-password');
/*
* 確認パスワードのキーボード（KeyUp）イベントリスナー
*/
elm_confirm.on('keyup', function () {
    // まだパスワード（確認）を入力していない
    if (elm_confirm.val() === "") {
        elm_confirm.removeClass("is-valid");
        elm_confirm.removeClass("is-invalid");
        return;
    }
    // 先頭から一文字ずつ取り出してチェックし最後まで到達していなくとも「問題無し」と判断
    var array_pass_chars = elm_pass.val().split("");
    var array_confirm_chars = elm_confirm.val().split("");
    $.each(array_confirm_chars, function (index, char) {
        if (array_pass_chars[index] === char) {
            // 先頭から一文字ずつ一致している場合には中途でも何も表示しない
            elm_confirm.removeClass("is-valid");
            elm_confirm.removeClass("is-invalid");
        }
        else {
            // 一文字でも異なる場合はInvalid
            elm_confirm.removeClass("is-valid");
            elm_confirm.addClass("is-invalid");
            return false;
        }
    });
    // 完全一致したらValid
    if (elm_pass.val() === elm_confirm.val()) {
        elm_confirm.addClass("is-valid");
    }
});
/*
* 確認パスワード入力のフォーカスを失ったとき（Blur）のイベントリスナー
*/
elm_confirm.on('blur', function () {
    // パスワード入力欄の両方が空のときはバリデーション表示を消す
    if (elm_pass.val() === "" && elm_confirm.val() === "") {
        elm_pass.removeClass('is-valid');
        elm_pass.removeClass('is-invalid');
        elm_confirm.removeClass('is-valid');
        elm_confirm.removeClass('is-invalid');
        return;
    }
    // 完全一致したらValid
    if (elm_pass.val() === elm_confirm.val()) {
        elm_confirm.removeClass('is-invalid');
        elm_confirm.addClass("is-valid");
    }
    else {
        // 一致しなかったらInvalid
        elm_confirm.removeClass('is-valid');
        elm_confirm.addClass("is-invalid");
    }
});
/*
* パスワード入力のフォーカスを失ったとき（Blur）のイベントリスナー
* 入力されたパスワードが適切なものかチェックする
*/
elm_pass.on('blur', function () {
    // パスワード入力欄の両方が空のときはバリデーション表示を消す
    if (elm_pass.val() === "" && elm_confirm.val() === "") {
        elm_pass.removeClass('is-valid');
        elm_pass.removeClass('is-invalid');
        elm_confirm.removeClass('is-valid');
        elm_confirm.removeClass('is-invalid');
        return;
    }
    var str = elm_pass.val();
    // 半角英数字をそれぞれ1種類以上含む8文字以上の文字列とマッチするか
    var result = str.match(/^(?=.*?[a-zA-Z])(?=.*?\d)[a-zA-Z\d]{8,}/);
    if (result) {
        // O.K.（Valid）
        elm_pass.removeClass('is-invalid');
        elm_pass.addClass('is-valid');
    }
    else {
        // 入力されたパスワードが一致しません。（Invalid）
        elm_pass.removeClass('is-valid');
        elm_pass.addClass('is-invalid');
    }
});

var elm_email = $('#email')
var elm_confirm_email = $('#confirm-email');
/*
* 確認emailのkeyup 
*/
elm_confirm_email.on('keyup', function () {
    // まだメールアドレス（確認）を入力していない
    if (elm_confirm_email.val() === "") {
        elm_confirm_email.removeClass("is-valid");
        elm_confirm_email.removeClass("is-invalid");
        return;
    }
    // 先頭から一文字ずつ取り出してチェックし最後まで到達していなくとも「問題無し」と判断
    var array_email_chars = elm_email.val().split("");
    var array_confirm_email_chars = elm_confirm_email.val().split("");
    $.each(array_confirm_email_chars, function (index, char) {
        if (array_email_chars[index] === char) {
            // 先頭から一文字ずつ一致している場合には中途でも何も表示しない
            elm_confirm_email.removeClass("is-valid");
            elm_confirm_email.removeClass("is-invalid");
        }
        else {
            // 一文字でも異なる場合はInvalid
            elm_confirm_email.removeClass("is-valid");
            elm_confirm_email.addClass("is-invalid");
            return false;
        }
    });
    // 完全一致したらValid
    if (elm_email.val() === elm_confirm_email.val()) {
        elm_confirm_email.addClass("is-valid");
    }
});
/*
* 確認メールアドレス入力のフォーカスを失ったとき（Blur）のイベントリスナー
*/
elm_confirm_email.on('blur', function () {
    // メールアドレス入力欄の両方が空のときはバリデーション表示を消す
    if (elm_email.val() === "" && elm_confirm_email.val() === "") {
        elm_email.removeClass('is-valid');
        elm_email.removeClass('is-invalid');
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.removeClass('is-invalid');
        return;
    }
    // 完全一致したらValid
    if (elm_email.val() === elm_confirm_email.val()) {
        elm_confirm_email.removeClass('is-invalid');
        elm_confirm_email.addClass("is-valid");
    }
    else {
        // 一致しなかったらInvalid
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.addClass("is-invalid");
    }
});
/*
* email入力のフォーカスを失ったとき（Blur）のイベントリスナー
* 入力されたメールアドレスが適切なものかチェックする
*/
elm_email.on('blur', function () {
    // email入力欄の両方が空のときはバリデーション表示を消す
    if (elm_email.val() === "" && elm_confirm_email.val() === "") {
        elm_email.removeClass('is-valid');
        elm_email.removeClass('is-invalid');
        elm_confirm_email.removeClass('is-valid');
        elm_confirm_email.removeClass('is-invalid');
        return;
    }
    var str = elm_email.val();
    // 半角英数字をそれぞれ1種類以上含む8文字以上の文字列とマッチするか
    //正規表現は、Microsoft社員限定に設定している。スタッフサインアップは変える必要
    var result = str.match(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}microsoft.com$/);
    if (result) {
        // O.K.（Valid）
        elm_email.removeClass('is-invalid');
        elm_email.addClass('is-valid');
    }
    else {
        // 入力されたアドレスが一致しません。（Invalid）
        elm_email.removeClass('is-valid');
        elm_email.addClass('is-invalid');
    }
});