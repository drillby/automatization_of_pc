import React, { useMemo, useEffect, useState } from "react";
import TimeShower from "../components/InfotainmentApp/TimeComponents/TimeShower";
import API from "../functions/InfotainmentApp/APIClient";

function Infotainment() {
	const api = useMemo(() => new API(), []);
	return <TimeShower api={api} />;
}

export default Infotainment;
