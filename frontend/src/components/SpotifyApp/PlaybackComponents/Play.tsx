import React from "react";
import { useState } from "react";
import API from "../../../functions/SpotifyApp/APIClient";
import PlayActive from "./PlayActive";
import { AiOutlineCaretDown, AiOutlineCaretUp } from "react-icons/ai";

function PlaySong(props: { api: API }) {
	const [active, setActive] = useState(false);

	return <>{PlaySelector()}</>;

	function PlaySelector() {
		return (
			<table className="w-full mt-4 h-8 outline bg-slate-300">
				<tbody>
					<tr
						onClick={() => setActive(!active)}
						className="hover:cursor-pointer hover:bg-slate-400 duration-500"
					>
						<td>
							<h1 className="text-left pl-2 font-medium h-8 pt-1">Přehrát</h1>
						</td>
						<td className="text-right w-6 outline">
							{active ? <AiOutlineCaretUp /> : <AiOutlineCaretDown />}
						</td>
					</tr>
					{active && (
						<tr>
							<td className="bg-white ">
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
