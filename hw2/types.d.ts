type ValidationResultType = {
  name: string;
  valid: boolean;
  message: string | null;
};

type CharDataType = {
  year: number;
  rank?: number;
};

type RankType = {
  rank: number;
  male: string | null;
  maleRankChange: number | null;
  female: string | null;
  femaleRankChange: number | null;
};

type FormType = {
  "first-name": HTMLInputElement;
  "last-name": HTMLInputElement;
  email: HTMLInputElement;
  "date-of-birth": HTMLInputElement;
};
