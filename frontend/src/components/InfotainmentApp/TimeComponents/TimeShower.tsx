import React from "react";
import API from "../../../functions/InfotainmentApp/APIClient";
import useDate from "../../../hooks/useDate";

function TimeShower(props: { api: API }) {
	const { date, time, wish } = useDate(1000);
	return (
		<div>
			<p>{date}</p>
			<p>{time}</p>
			<p>{wish}</p>
		</div>
	);
}

export default TimeShower;
