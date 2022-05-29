import React from "react";
import API from "../functions/APIClient";

function VolumeSlider(props: { api: API }) {
	return (
		<>
			<table>
				<tbody>
					<tr>
						<td>
							<button>-</button>
						</td>
						<td>0</td>
						<td>
							<input type="range" name="" id="" min="0" max="100" />
						</td>
						<td>100</td>
						<td>
							<button>+</button>
						</td>
					</tr>
				</tbody>
			</table>
		</>
	);
}

export default VolumeSlider;
