import React, { useMemo, useEffect, useState } from "react";
import API from "../functions/InfotainmentApp/APIClient";

function Infotainment() {
	const api = useMemo(() => new API(), []);
	return <div className="outline">Infotainment</div>;
}

export default Infotainment;
