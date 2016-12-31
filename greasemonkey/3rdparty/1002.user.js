// ==UserScript==
// @name        网盘自动填写提取密码
// @namespace   http://jixun.org/
// @description 自动填写提取密码，失败不重试。
// @include     http://pan.baidu.com/share/init?*
// @include     http://yun.baidu.com/share/init?*
// @include     https://pan.baidu.com/share/init?*
// @include     https://yun.baidu.com/share/init?*
// @include     https://eyun.baidu.com/enterprise/share/init?*

// @include     http://*.yunpan.cn/lk/*
// @include     https://*.yunpan.cn/lk/*
// @include     http://share.weiyun.com/*
// @version     1.0.3.5
// @grant       none
// @run-at      document-start
// ==/UserScript==

(function ($) {
	var site = {
		'yunpan.cn': {
			chk:  /^[a-z0-9]{4}$/i,
			code: '.pwd-input',
			btn:  '.submit-btn'
		},
		'baidu.com': {
			chk:  /^[a-z0-9]{4}$/i,
			code: '#accessCode, .share-access-code',
			btn:  '#submitBtn, a[node-type="share-access-btn"]'
		},
        'weiyun.com': {
            chk: /^[a-z0-9]{4}$/i,
			code: '#outlink_pwd',
			btn:  '#outlink_pwd_ok'
        }
	};

	addEventListener ('DOMContentLoaded', function () {
		// 抓取提取码
		var sCode = location.hash.slice(1).trim(),
			hostName = location.host.match(/\w+\.\w+$/)[0].toLowerCase();

		var conf = site[hostName];

		// 检查是否为合法格式
		if (!conf || !conf.chk.test(sCode))
			// 没有 Key 或格式不对
			return ;

		// 调试用
		console.log ('抓取到的提取码: %s', sCode);

		// 加个小延时
		setTimeout (function () {
			// 键入提取码并单击「提交」按钮，报错不用理。
			var codeBox = $(conf.code),
				btnOk = $(conf.btn);

			if (codeBox) codeBox.value = sCode;

			if (conf.preSubmit)
				if (conf.preSubmit (codeBox, btnOk, sCode))
					return ;

			if (btnOk) btnOk.click();
		}, 10);
	}, false);
})(function ($) {
	return document.querySelector ($);
});
