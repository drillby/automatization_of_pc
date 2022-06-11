import React from "react";
import "../index.css";
import loadingIcon from "../svgs/find-magnifier-magnifying-glass-svgrepo-com.svg";

function Tests() {
	return (
		<img
			className="sm:animation-loading-spotify m-auto mt-40 animate-pulse"
			width={200}
			src={loadingIcon}
			alt=""
		/>
	);
}

export default Tests;
