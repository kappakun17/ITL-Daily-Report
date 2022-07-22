/ JavaScript source code 

//rollAnimeにrollというクラス名を付ける定義 

function RollAnimeControl() {

    $('.rollAnime').each(function () {

        var elemPos = $(this).offset().top - 50;

        var scroll = $(window).scrollTop();

        var windowHeight = $(window).height();

        var childs = $(this).children();  //rollAnimeの子要素を取得 

        if (scroll >= elemPos - windowHeight) {

            $(childs).each(function (i) {   //子要素を1つ1つ処理をおこなう 

                if (i < 10) {         //10未満の場合 

                    $(this).css("transition-delay", "." + i + "s");  //子要素にcsstransition-delayを追加 

                } else {             //10以上の場合 

                    var n = i / 10;       //ミリ秒指定なので10で割る 

                    $(this).css("transition-delay", n + "s");  //子要素にcsstransition-delayを追加 

                }

            });



            $(this).addClass("roll"); //rollというアニメーションクラスを付与 



        } else {

            $(childs).each(function () {    //子要素を1つ1つ処理をおこなう 

                $(this).css("transition-delay", "0s");//子要素にcsstransition-delayの秒を0とする 

            });

            $(this).removeClass("roll");//rollというアニメーションクラスを除去 

        }

    });

}