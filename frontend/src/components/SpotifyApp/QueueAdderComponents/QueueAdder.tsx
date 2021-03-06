import React, { useState } from "react";
import { AiOutlineCaretDown, AiOutlineCaretUp } from "react-icons/ai";
import API from "../../../functions/SpotifyApp/APIClient";
import QueueAdderActive from "./QueueAdderActive";

function QueueAdder(props: { api: API }) {
	const [active, setActive] = useState(false);
	return (
		<table className="w-full mt-4 h-8 outline bg-slate-300">
			<tbody>
				<tr
					onClick={() => setActive(!active)}
					className="hover:cursor-pointer hover:bg-slate-400 duration-500"
				>
					<td>
						<h1 className="text-left pl-2 font-medium h-8 pt-1">
							Přidat do fronty
						</h1>
					</td>
					<td className="text-right w-6">
						{active ? <AiOutlineCaretUp /> : <AiOutlineCaretDown />}
					</td>
				</tr>
				{active && (
					<tr>
						<td className="bg-white">
							<QueueAdderActive api={props.api} state={setActive} />
						</td>
						<td className="bg-white"></td>
					</tr>
				)}
			</tbody>
		</table>
	);
}

export default QueueAdder;
