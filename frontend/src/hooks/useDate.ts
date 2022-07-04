import { useEffect, useState } from "react";
import useDateType from "../types/hookTypes/useDateType";

/**
 * 
 * @param interval time in ms
 * @param country what language you want to return date in
 * @returns date, time, wish
 */
export default function useDate(interval: number, country: string): useDateType {
    const [today, setDate] = useState(new Date())

    useEffect(() => {
        const timer = setInterval(() => {
            setDate(new Date())
        }, interval);
        return () => {
            clearInterval(timer)
        }
    }, [interval])

    const day = today.toLocaleDateString(country, { weekday: "long" })
    const date = `${day}`;
    const hour = today.getHours()

    var wish = "Dobrý den"
    if (hour < 9) {
        wish = "Dobré ráno"
    }
    else if (hour >= 9 && hour <= 12) {
        wish = "Dobré dopoledne"
    }
    else if (hour === 12) {
        wish = "Dobré poledne"
    }
    else if (hour > 12 && hour <= 18) {
        wish = "Dobré odpoledne"
    }
    else {
        wish = "Dobrý večer"
    }
    const time = today.toLocaleDateString(country, { hour: "numeric", hour12: false, minute: "numeric" })

    return {
        date,
        time,
        wish
    }
}