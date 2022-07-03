import React from "react";
import useDate from "../../../hooks/useDate";

function TimeShower() {
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
