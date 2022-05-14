function changeHeadInfo(title: string, cover: string) {
	document.title = title;
	const coverElement = document.querySelector("link");
	if (coverElement) {
		coverElement.setAttribute("href", cover);
	}
}

export default changeHeadInfo;
