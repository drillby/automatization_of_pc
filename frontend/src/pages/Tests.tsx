import React, { useState, useEffect } from "react";
import "../index.css";
import loadingIcon from "../svgs/find-magnifier-magnifying-glass-svgrepo-com.svg";

function Tests() {
	const [isActive, setIsActive] = useState(false);

	useEffect(() => {
		console.log(isActive, "useEffect");
		if (isActive) {
			console.log("isActive");
			document
				.getElementById("colapsable-icon")
				?.classList.remove("animation-colapsable-icon-inactive");
			document
				.getElementById("colapsable-icon")
				?.classList.add("animation-colapsable-icon-active");
			// permanently aply rotation to the icon
		} else {
			console.log("notActive");
			document
				.getElementById("colapsable-icon")
				?.classList.add("animation-colapsable-icon-inactive");
			document
				.getElementById("colapsable-icon")
				?.classList.remove("animation-colapsable-icon-active");
		}
	}, [isActive]);
	return (
		<img
			className="m-auto mt-40"
			width={200}
			src={loadingIcon}
			alt=""
			id="colapsable-icon"
			onClick={() => setIsActive(!isActive)}
		/>
	);
}

export default Tests;
