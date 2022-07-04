import React from "react";
import useDate from "../../../hooks/useDate";

function TimeShower() {
	const { date, time, wish } = useDate(5 * 1000, "cs", false);
	return (
		<div className="outline text-center">
			<h1 className="">{wish}</h1>
			<p>{date}</p>
			<p>{time}</p>
		</div>
	);
}

export default TimeShower;
