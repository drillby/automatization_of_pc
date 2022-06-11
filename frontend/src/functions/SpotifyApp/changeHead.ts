function changeHeadInfo(title: string, cover: string) {
	const coverElement = document.querySelector("link");
	if (coverElement) {
		document.title = title;
		coverElement.setAttribute("href", cover);
	}
}

export default changeHeadInfo;
