import React from "react";
import { useState } from "react";
import { AiOutlineCaretDown } from "react-icons/ai";
import { AiOutlineCaretUp } from "react-icons/ai";
import API from "../functions/APIClient";
import PlayActive from "./PlayActive";

function PlaySong(props: { api: API }) {
	const [active, setActive] = useState(false);

	return <>{PlaySelector()}</>;

	function PlaySelector() {
		return (
			<table className="w-full mt-4 h-8 outline bg-slate-100">
				<tbody>
					<tr
						onClick={() => setActive(!active)}
						className="hover:cursor-pointer hover:bg-slate-400"
					>
						<td>
							<h1 className="text-left pl-2 font-medium h-8 pt-1">Přehrát</h1>
						</td>
						<td className="text-right w-6">
							{active ? <AiOutlineCaretUp /> : <AiOutlineCaretDown />}
						</td>
					</tr>
					{active && (
						<tr>
							<td className="bg-white">
								<PlayActive api={props.api} state={setActive} />
							</td>
							<td className="bg-white"></td>
						</tr>
					)}
				</tbody>
			</table>
		);
	}
}

export default PlaySong;
