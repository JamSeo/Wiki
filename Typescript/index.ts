

type N = { name : string}
type M = { name : string, age: number}
type NM = N & M

let person :NM = { name:'kim', age:20}


type Color = { 
	color? : string, 
	size : number,
	readonly position : number[],
}


type Info = { name:string, phone:number, email:string}
let 인간 :Info = { name : 'kim', phone : 123, email : 'abc@naver.com' }

type 미성년자여부 = {미성년자:boolean};
type NewInfo = Info & 미성년자여부

let 회원가입정보 :NewInfo = {
	name : 'kim', 
	phone : 123, 
	email : 'abc@naver.com',
	미성년자 : true,
}