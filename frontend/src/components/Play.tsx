import React from "react";
import { useState } from "react";
import { AiOutlineCaretDown } from "react-icons/ai";
import { AiOutlineCaretUp } from "react-icons/ai";
import PlayActive from "./PlayActive";

function PlaySong() {
	const [active, setActive] = useState(false);

	return <div>{PlaySelector()}</div>;

	function PlaySelector() {
		return (
			<table className="w-full mt-4 h-8 outline bg-slate-100">
				<tbody>
					<tr onClick={() => setActive(!active)}>
						<td>
							<h1 className="text-left pl-2 font-medium h-8 pt-1">Přehrát</h1>
						</td>
						<td className="text-right w-6">
							{active ? <AiOutlineCaretUp /> : <AiOutlineCaretDown />}
						</td>
					</tr>
					<tr>
						<td className="bg-white">{active && <PlayActive />}</td>
						<td className="bg-white"></td>
					</tr>
				</tbody>
			</table>
		);
	}
}

export default PlaySong;
