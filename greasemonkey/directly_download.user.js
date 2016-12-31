// ==UserScript==
// @name          绕过itpub二维码下载
// @description   绕过二维码验证直接下载itpub附件
// @author        chunchengfh
//
// @include       http://www.itpub.net/*
// @include       https://www.itpub.net/*
//
// @grant         unsafeWindow
// @encoding      utf-8
// @run-at        document-idle
//
// ==/UserScript==


//var attaches = document.getElementsByClassName('attnm');  // Why does this fail??
var attaches = document.getElementsByTagName('a');

for (var i=0; i<attaches.length; i++) {
	var at = attaches[i];
	//console.log(at.href);
	if ((/attachment.php\?aid=/i).test(at.href)) {
		//console.log(at.href);
		at.href = at.href.replace("attachment.php\?aid=", "forum.php?mod=attachment&aid=");
		//console.log(at.href);
	}
}
