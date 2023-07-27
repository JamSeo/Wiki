let 링크들 = document.querySelectorAll('.naver')

링크들.forEach((링크) => {
    if (링크 instanceof HTMLAnchorElement){
        링크.href = 'https://kakao.com'
    }
})